# 🎉 Birthday & Celebration Reminder (Jalali Calendar)

A Django app to save birthdays (in **Jalali/Shamsi**) of important people and pick custom celebration dates.  
Built with **django_jalali** to handle Jalali dates seamlessly inside Django + PostgreSQL.

---

## 🚀 Features
- Use `jDateField` from `django_jalali` for Jalali support.
- Dates are stored as real `DateField` in PostgreSQL, fully compatible with queries.
- Two tabs:
  - **List of People** → show all people with their Jalali birth date + celebration date.
  - **Add Person** → form to add new person with Jalali calendar widget.
- Countdown to next celebration.
- Clean and simple UI.

---

## 🛠️ Tech Stack
- [Django](https://www.djangoproject.com/) — backend framework
- [django_jalali](https://pypi.org/project/django-jalali/) — Jalali model fields & form widgets
- [PostgreSQL](https://www.postgresql.org/) — database
- Optional: Jalali datepicker (frontend) for nicer UX

---