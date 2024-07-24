from google.cloud import dataproc_v1
from google.protobuf import duration_pb2


def main(
    project_id: str, 
    region: str, 
    bucket_name: str, 
    subnet: str, 
    batch_id: str
):
    print('## Running Batch..')

    pyspark_file = f"gs://{bucket_name}/code/wordcount_v3.py"

    # initialize a client
    client = dataproc_v1.BatchControllerClient(client_options={
        'api_endpoint': f'{region}-dataproc.googleapis.com:443'
    })

    # Configure the batch
    batch = {
        'pyspark_batch': {
            'main_python_file_uri': pyspark_file,
            # 'jar_file_uris': ["gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.29.0.jar"]
        },
        'environment_config': {
            'execution_config': {
                'subnetwork_uri': f"projects/{project_id}/regions/{region}/subnetworks/{subnet}"
            }
        },
        'runtime_config': {
            'version': "2.1" # otherwise we'll get a jar error
        }
    }

    # specify the request
    request = dataproc_v1.CreateBatchRequest(
        parent=f"projects/{project_id}/regions/{region}",
        batch=batch,
        batch_id=batch_id
    )

    try:
        # submitting the batch
        operation = client.create_batch(request=request)
        response = operation.result()

        print(f"Batch job '{batch_id}' submitted successfully.")
    except Exception as e:
        print(f"Error submitting batch job: {e}")

if __name__ == '__main__':

    # set variables
    PROJECT_ID = "project"
    REGION = "us-central1"
    BUCKET = "kb-wc"
    SUBNET = "default"
    BATCH_ID = "wc-id1"

    main(PROJECT_ID, REGION, BUCKET, SUBNET, BATCH_ID)
    
