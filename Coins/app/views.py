from django.shortcuts import render
from .models import Student
from datetime import date
STUDENT_STATUS = dict()
STUDENT_COINS = dict()
def get_august_dates():
    days = []
    for i in range(2, 32, 2):
        days.append(date(2025, 8, i))
    return days
def home(request):
    students = Student.objects.all()
    dates = get_august_dates()
    max_daily = 350
    if request.method == "POST":
        for s in students:
            sid = str(s.id)
            c = request.POST.get('coins_' + sid)
            if c:
                try:
                    c = int(c)
                except:
                    c = 0
                if not sid in STUDENT_COINS:
                    STUDENT_COINS[sid] = {'today': 0, 'total': 0}
                if STUDENT_COINS[sid]['today'] + c <= max_daily:
                    STUDENT_COINS[sid]['today'] += c
                    STUDENT_COINS[sid]['total'] += c
            for d in dates:
                key = f'status_{sid}_{d}'
                value = request.POST.get(key)
                if value == 'Yes' or value == 'No':
                    if sid not in STUDENT_STATUS:
                        STUDENT_STATUS[sid] = {}
                    STUDENT_STATUS[sid][str(d)] = value
    result = []
    for s in students:
        sid = str(s.id)
        coins = STUDENT_COINS.get(sid, {'today': 0, 'total': 0})
        att = []
        for d in dates:
            d_str = str(d)
            status = ''
            if sid in STUDENT_STATUS and d_str in STUDENT_STATUS[sid]:
                status = STUDENT_STATUS[sid][d_str]
            att.append({'date': d_str, 'status': status})
        result.append({'student': s, 'attendances': att, 'today_coins': coins['today'], 'total_coins': coins['total']})
    return render(request, 'home.html', {'student_rows': result, 'august_dates': dates, 'max_daily_coins': max_daily})
