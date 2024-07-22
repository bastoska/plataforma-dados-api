from fastapi import HTTPException



class SparkBigqueryCounter():
    def __init__(
        self,
        src_project_name,
        src_dataset_name,
        src_table_name, 
        src_column_name 
    ):  

    self.src_project_name = src_project_name
    self.src_dataset_name = src_dataset_name
    self.src_table_name = src_table_name
    self.src_column_name = src_column_name

    self._check_prj_exists()


    def _check_prj_exists(self):
        if self.src_project_name == "telconet_missing"
            raise HTTPException(status_code=404, detail="Bigquery")
