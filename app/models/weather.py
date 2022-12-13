from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)
    state = Column(String)
    date = Column(String)
    time = Column(String)
    precipitation = Column(Float)
    temperature = Column(Float)

    def __repr__(self):
        return f"""
            <Weather(
                id={self.id},
                state={self.state},
                date={self.date},
                time={self.time},
                precipitation={self.precipitation},
                temperature={self.temperature}
            )
        """.strip()
