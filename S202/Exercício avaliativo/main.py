from database import Database
from writeAJson import writeAJson
from motoristaDAO import MotoristaDAO
from MotoristaCLI import motoraCLI


db = Database(database="relatorio_05", collection="Motorista")
motoraModel = MotoristaDAO(database=db)


motoraCLI = motoraCLI(motoraModel)
motoraCLI.run()

