import os
import pickle
from settings import INITIAL_ID


class ControlIdRepository:

    def __init__(self):
        self._initial_id = INITIAL_ID
        self._last_id = None
        self._pkl_file = 'control_id.pkl'
    
    def _set(self, id: int) -> None:
        file = open(self._pkl_file, 'wb')
        pickle.dump(id, file)
        file.close()
    
    def get(self) -> int:

        if os.path.exists(self._pkl_file):
            file = open(self._pkl_file, 'rb')
            self._last_id = pickle.load(file)
            file.close()
            return self._last_id
        
        return self._initial_id
   
    def reset(self) -> None:
        self._set(self._initial_id)
        self._last_id = None
    
    def save(self, id: int):
        self._set(id)
        self._last_id = id