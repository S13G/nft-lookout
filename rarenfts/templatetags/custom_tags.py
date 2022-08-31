from django import template
register = template.Library()



@register.filter
def in_date(collections, day):
    return collections.filter(date=day)


@register.filter
def in_date_limited(collections, day):
    return in_date(collections, day)[:15]



@register.filter
def count_col(collections, day):
    return in_date(collections, day).count()


@register.filter
def limit_result(collection):
    return collection.filter(collection)

months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

@register.filter
def dt_format(day):
    month = months[day.month]
    date = day.day

    return f'{month} {date}'