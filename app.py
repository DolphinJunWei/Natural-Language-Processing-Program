#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template


# In[4]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        print(file)
        filename = file.filename
        print(filename)
        a= file.save("excel/" + filename)
        s = "Thank you for using our service. The cleaned CSV file and Summary Visualisations have been sent to you."
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




