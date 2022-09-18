from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, SMALLINT
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(200))
    email = Column(String(50))
    created_at = Column(String)
    updated_at = Column(String)
    deleted_at = Column(String)
    income = Column(Numeric, nullable=False)
    banking_data = relationship('BankingData', backref='user', lazy='subquery')


class BankingData(Base):
    __tablename__ = 'banking-data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bank_name = Column(String(50), nullable=False)
    bank_code = Column(SMALLINT, nullable=False)
    bank_branch = Column(Integer, nullable=False)
    account_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(String)
    deleted_at = Column(String)
