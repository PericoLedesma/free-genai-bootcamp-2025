# Defines the database models. Each model is a class that inherits from Base class.

# Base class is the declarative base class from SQLAlchemy.
# It is a class that is returned by declarative_base() function.

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True, index=True)
    german = Column(String, index=True)
    english = Column(String, index=True)
    parts = Column(String)

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class WordGroup(Base):
    __tablename__ = 'words_groups'
    id = Column(Integer, primary_key=True, index=True)
    word_id = Column(Integer, ForeignKey('words.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))

class StudySession(Base):
    __tablename__ = 'study_sessions'
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    created_at = Column(DateTime)
    study_activity_id = Column(Integer, ForeignKey('study_activities.id'))

class StudyActivity(Base):
    __tablename__ = 'study_activities'
    id = Column(Integer, primary_key=True, index=True)
    study_session_id = Column(Integer, ForeignKey('study_sessions.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))
    created_at = Column(DateTime)

class WordReviewItem(Base):
    __tablename__ = 'word_review_items'
    word_id = Column(Integer, ForeignKey('words.id'))
    study_session_id = Column(Integer, ForeignKey('study_sessions.id'))
    correct = Column(Boolean)
    created_at = Column(DateTime)