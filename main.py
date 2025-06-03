from apscheduler.schedulers.blocking import BlockingScheduler
from news_scraper import scrape_financial_news
from summarizer import summarize_and_analyze
from emailer import format_email, send_email
from config import EMAIL_RECIPIENT

def run_macro_digest():
    articles = scrape_financial_news()
    summaries = [summarize_and_analyze(article) for article in articles]
    sorted_summaries = sorted(summaries, key=lambda x: x['importance'], reverse=True)
    html_content = format_email(sorted_summaries)
    send_email(subject="📊 Daily Macro Update", html_body=html_content, recipient=EMAIL_RECIPIENT)

scheduler = BlockingScheduler(timezone="Europe/London")
scheduler.add_job(run_macro_digest, 'cron', hour=5)
scheduler.start()