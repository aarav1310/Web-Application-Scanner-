from pyzap import ZAP

def scan_website(url):
    zap=ZAP
    zap.urlopen(url)
    zap.spider.scan(url)
    zap.ajaxSpider.scan(url)
    zap.active_scan.scan_as_user(url)
    zap.ajaxSpider.results()
    zap.spider.results()
    zap.core.alerts()
target_url='http:/anyurl.com'
scan_website(target_url)