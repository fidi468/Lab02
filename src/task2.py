class BrowserHistory:
    def __init__(self):
        self.stack = []                    
    def visit(self, page):
        self.stack.append(page)              
        print("Açıldı:", page)
    def back(self):
        if len(self.stack) > 1:
            self.stack.pop()                
            print("Geri qayıdıldı:", self.stack[-1])
        else:
            print("Geri qayıtmaq mümkün deyil")

    def current(self):
        return self.stack[-1] if self.stack else None

browser = BrowserHistory()
browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("github.com")
browser.back()
browser.back()                            
print("Hazırkı səhifə:", browser.current())
browser.back()                               
