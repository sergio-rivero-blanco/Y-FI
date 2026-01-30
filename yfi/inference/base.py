from abc import ABC, abstractclassmethod

class BaseInferenceProvider(ABC):
    @abstractclassmethod
    def infer(self, file_path: str, doc_type: str) -> dict:
        pass