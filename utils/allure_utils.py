import json
import os
import subprocess

def parse_allure_results(results_dir: str):
    """Собирает краткую статистику из allure-results."""
    summary = {
        "passed": 0,
        "failed": 0,
        "broken": 0,
        "skipped": 0,
        "total": 0,
        "report_url": "https://niyaz-ananev-khayrullayevich.github.io/AllureTest/"  
    }

    # Опционально: сгенерировать отчёт
    subprocess.run(
        ["allure", "generate", results_dir, "-o", "allure-reports", "--clean"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Прочитаем файлы JSON из allure-results
    for file in os.listdir(results_dir):
        if file.endswith("-result.json"):
            with open(os.path.join(results_dir, file)) as f:
                data = json.load(f)
                status = data.get("status", "")
                if status in summary:
                    summary[status] += 1
                summary["total"] += 1

    return summary
