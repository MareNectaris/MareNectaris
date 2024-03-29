import feedparser, datetime

tistory_blog_uri="https://blog.stdio.dev"
feed = feedparser.parse(tistory_blog_uri+"/rss")

markdown_text = """# Hello, there!
![iidx at solved.ac](https://github-readme-solvedac.hyp3rflow.vercel.app/api/?handle=iidx)<br>
<em>still</em> an amateur developer wandering around the digital world<br>
## Recent blog posts
""" # list of blog posts will be appended here

lst = []


for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
