import mysql.connector
from repositories.control_id_repository import ControlIdRepository
from settings import DB_CONFIG


class CallRepository:
    
    def __init__(self) -> None:
        self._db = None
        self._control_id = ControlIdRepository()

    def get_abandon_callers(self) -> list:
        abandon_callers = []
        initial_id = self._control_id.get()
        self.connect()
        
        for id, callid in self._get_abandon_calls_ids(initial_id):
            phone_number = self._get_phone_number(callid)

            if phone_number and phone_number not in abandon_callers:
                abandon_callers.append(phone_number)

            id += 1
            self._control_id.save(id)
        
        self.close()
        return abandon_callers

    def _get_abandon_calls_ids(self, initial_id: int) -> list:
        mycursor = self._db.cursor()
        query = f"SELECT id, callid FROM queue_log WHERE event='ABANDON' AND id >= {initial_id}"
        mycursor.execute(query)
        results = mycursor.fetchall()
        mycursor.close()
        return results
    
    def _get_phone_number(self, callid) -> str:

        try:
            mycursor = self._db.cursor()
            query = f"SELECT data2 FROM queue_log WHERE event='ENTERQUEUE' AND callid='{callid}'"
            mycursor.execute(query)
            phone_number, = mycursor.fetchone()
            mycursor.close()
            return phone_number
        
        except:
            return None
    
    def connect(self):
        self._db = mysql.connector.connect(
            host=DB_CONFIG['HOST'],
            user=DB_CONFIG['USER'],
            password=DB_CONFIG['PASSWORD'],
            database=DB_CONFIG['DATABASE'],
            auth_plugin='mysql_native_password'
        )

    def close(self):
        self._db.close()