from datetime import datetime


def generate_filename(report_type):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{report_type}_{timestamp}"