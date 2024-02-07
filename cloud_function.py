from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "gcp-pro-1-dev"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "cricbuzz-bqload-job-dev",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://cricbuzz-pipeline-metadata/udf.js",
        "JSONPath": "gs://cricbuzz-pipeline-metadata/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "gcp-pro-1-dev:circbuzz_dataset.batsmen_ranking_table",
        "inputFilePattern": "gs://cricbuzz_buket/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://cricbuzz-pipeline-metadata",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)