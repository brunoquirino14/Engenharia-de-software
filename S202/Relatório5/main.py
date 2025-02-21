from database import Database
from writeAJson import writeAJson
from bookModel import BookModel
from cli import BooksCLI

db = Database(database="DbLivros", collection="Livros")
db.resetDatabase()
bookModel = BookModel(database=db)


BooksCLI = BooksCLI(bookModel)
BooksCLI.run()
