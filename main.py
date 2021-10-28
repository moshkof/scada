# demo: механизм ответа modbus_tcp
import modbus_tk.defines as md
import modbus_tk.modbus_tcp as mt
import tracemalloc

 
class ConfigModbus(object):
    host = "192.168.19.35"
    port = 502


# Создать объект подключения
master = mt.TcpMaster(ConfigModbus.host, ConfigModbus.port)
master.set_timeout(2.5)

print('соединение успешно установлено ')

try:
    # master.execute удаленно подключиться к серверу
    # Определить, нормальная ли ссылка
    
    tracemalloc.start()
    START_POS =0 # отправная точка
    MAX_LENGTH = 16 # Количество цифр
    Result = []
    # md.READ_HOLDING_REGISTERS # Modbus чтение регистра временного хранения 3
    def read_holding_regist():
        for i in range(10, 13):
            # await asyncio.sleep(1)
            try:
                
                if i == 11:
                    pass
                Hold_value = master.execute(slave=i, function_code=md.READ_HOLDING_REGISTERS, starting_address=START_POS,
                                    quantity_of_x=MAX_LENGTH)
                # coils_value = master.execute(slave=i, function_code=md.READ_COILS, starting_address=START_POS, quantity_of_x=MAX_LENGTH)
                Result.append(i)
                Result.append(Hold_value)
                print(i, Hold_value)
                # print(coils_value)
            except Exception as e:
                print(i, e)
                continue


except Exception as e:
    print("error:", e)
    

if __name__ == "__main__":
    read_holding_regist()
    print("Конец программы")
    print(Result)