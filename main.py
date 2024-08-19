import json
from utils.pdf_utils import create_pdf


def main():
    with open('data/report_data.json') as f:
        data = json.load(f)

    create_pdf(data, "output_report.pdf")


if __name__ == "__main__":
    main()
