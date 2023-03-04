from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



Base = declarative_base()





class CoreBodyPart(Base):
    __tablename__ = "core_body_parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    image_url = Column(String)
    sub_body_parts = relationship("SubBodyPart", back_populates="core_body_part")

    def __repr__(self):
        return f"CoreBodyPart(id={self.id!r}, name={self.name!r}, description={self.description!r})"



class SubBodyPart(Base):
    __tablename__ = "sub_body_parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    core_body_part_id = Column(Integer, ForeignKey("core_body_parts.id"))
    core_body_part = relationship("CoreBodyPart", back_populates="sub_body_parts")
    exercises = relationship("Exercise", back_populates="sub_body_part")

    def __repr__(self):
        return f"SubBodyPart(id={self.id}, name={self.name}, description={self.description}, core_body_part_id={self.core_body_part_id})"


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    animation_url = Column(String)
    sub_body_part_id = Column(Integer, ForeignKey("sub_body_parts.id"))
    sub_body_part = relationship("SubBodyPart", back_populates="exercises")

    def __repr__(self):
        return f"Exercise(id={self.id}, name={self.name}, description={self.description}, sub_body_part_id={self.sub_body_part_id})"
