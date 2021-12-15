def hugging_face(input_txt,opt):
    from transformers import pipeline
    from bs4 import BeautifulSoup
    import requests

    summarizer=pipeline('summarization')

    if opt ==1 :
        URL =input_txt
        # URL="https://hackernoon.com/an-introduction-to-the-internet-computer"
        r=requests.get(URL)
        #r.text
        soup = BeautifulSoup(r.text, 'html.parser')
        results = soup.find_all(['h1', 'p','h2'])
        text =[result.text for result in results]
        ARTICLE = ' '.join(text)
    else :
        ARTICLE = input_txt

    max_chunk= 400
    ARTICLE = ARTICLE.replace('.', '.<eos>')
    ARTICLE = ARTICLE.replace('?', '?<eos>')
    ARTICLE = ARTICLE.replace('!', '!<eos>')

    sentences = ARTICLE.split('<eos>')
    current_chunk = 0 
    chunks = []
    for sentence in sentences:
       if len(chunks) == current_chunk + 1: 
          if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
             chunks[current_chunk].extend(sentence.split(' '))
          else:
             current_chunk += 1
             chunks.append(sentence.split(' '))
       else:
           print(current_chunk)
           chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
       chunks[chunk_id] = ' '.join(chunks[chunk_id])
      #len(chunks)
    res = summarizer(chunks, max_length=40, min_length=10, do_sample=False)
    #print(res)

    text = ' '.join([summ['summary_text'] for summ in res])
    return text
hugging_face("https://hackernoon.com/an-introduction-to-the-internet-computer",1)