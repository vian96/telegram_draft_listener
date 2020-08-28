#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import pyrogram
from telegraph import Telegraph
import config


app = pyrogram.Client(config.name, config.api_id, config.api_hash)
tlgraph = Telegraph(config.tlgraph_token)

def slice_to_first_char(s1, s2):
    for i, c in enumerate(s1):
        if c in s2:
            return s1[:i+1]
    return s1

@app.on_raw_update() 
def draft_update(client, update, users, chats):
    try:
        try:
            txt = update.draft.message # check if update is draft
        except:
            return

        # check if draft is what we need
        if len(txt)<50: 
            return
        for txt_start in ["pasta", "Pasta", "паста", "Паста", ]: 
            if txt.startswith(txt_start):
                break
        else:
            return
        mes = app.send_message('me', 'got pasta')


        txt = txt[len('pasta')+1:]

        # formatting \n for html
        for i in range(10): 
            txt = txt.replace('\n' + ' '*i + '\n', '\n\n')
        while txt != (txt:=txt.replace('\n'*3, '\n\n')):
            pass
        
        # getting title
        title=txt[:min(250, len(txt))]
        for title_start in ['назв', 'название', 'name', 'title', ]: # user writes his own title
            srch = '&'+title_start+'&'
            if title.startswith(srch):
                title, txt = title[len(srch) : title.find(srch, 2)], txt[len(srch)+title.find(srch, 2):]
                break  
        else:   # creating title from text
            title = slice_to_first_char(title, "\n.!?")
            if title[-1]=='.':
                title=title[:-2]


        res = tlgraph.create_page(
            title, None,
            "<p>" + txt.replace('\n'*2, '</p><p>').replace('\n', '<br/>')+'</p>', # creating html page
            'Author name', "Author link"
        )
        mes.edit_text(res['url'], parse_mode=None)

    except Exception as e:
        app.send_message('me', e)


app.run()
