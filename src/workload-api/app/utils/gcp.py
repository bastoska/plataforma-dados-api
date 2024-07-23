from fastapi import HTTPException


class SparkBigqueryCounter():
    """
    A class to handle the wordcount workloads.
    (TODO)
    """
    def __init__(
        self,
        src_project,
        src_dataset,
        src_table, 
        src_column_name,
        **kwargs
    ):  

        self.src_project = src_project
        self.src_dataset = src_dataset
        self.src_table = src_table
        self.src_column_name = src_column_name

        self._check_exists()


    def _check_exists(self):
        """
        This method only for simulation purposes. The idea is to
        demonstrate a failure in case of inexistence of one of the following in BigQuery:
            - dataset
            - project
            - table
        """
        if self.src_project == "telconet_missing_project":
            raise HTTPException(status_code=404, detail="Bigquery Source Project doest not exist")
        if self.src_dataset == "telconet_missing_dataset":
            raise HTTPException(status_code=404, detail="Bigquery Source Dataset doest not exist")
        if self.src_table == "telconet_missing_table":
            raise HTTPException(status_code=404, detail="Bigquery Source Table doest not exist")
    
    def send_job(self):
        """
        Sends the job to execution.
            - send to a pub/sub for a function to read (required the pub/sub conn) and then create a dataproc job/batch
            
        """
        pass
