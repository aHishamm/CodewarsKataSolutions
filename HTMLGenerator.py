class HTMLGen: 
    def a(self, string):
        self.string = string
        return "<a>"+self.string+"</a>"
    
    def b(self, string):
        self.string = string
        return "<b>"+self.string+"</b>"

    def p(self, string):
        self.string = string 
        return "<p>"+self.string+"</p>"

    def body(self, string):
        self.string = string 
        return "<body>"+self.string+"</body>"

    def div(self,string):
        self.string = string
        return "<div>"+self.string+"</div>"

    def span(self, string):
        self.string = string 
        return "<span>"+self.string+"</span>"
    
    def title(self, string): 
        self.string = string 
        return "<title>"+self.string+"</title>"
    
    def comment(self, string):
        self.string = string 
        return "<!--"+self.string+"-->"



