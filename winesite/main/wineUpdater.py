from .models import Wine


def add(w_name, w_winery, w_date, w_price): #for w_date use datetime.utcnow()!!!
    w = Wine(name=w_name, winery=w_winery, crawl_date=w_date, price=w_price)
    w.save()
