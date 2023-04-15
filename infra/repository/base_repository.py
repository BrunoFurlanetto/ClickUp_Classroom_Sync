from sqlalchemy import and_

from infra.configs.connections import DBConnectionHandler


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def filter(self, **kwargs):
        with DBConnectionHandler() as db:
            filter_fields = self.__verify_filter_fields(**kwargs)
            data = db.session.query(self.model).filter(and_(*filter_fields))

        return data.all()

    def get(self, **kwargs):
        with DBConnectionHandler() as db:
            filter_fields = self.__verify_filter_fields(**kwargs)
            data = db.session.query(self.model).filter(and_(*filter_fields))

        if len(data.all()) > 1:
            raise ValueError("Expected one result, but got multiple results.")

        if len(data.all()) == 0:
            return None

        return data[0]

    def insert(self, **kwargs):

        with DBConnectionHandler() as db:
            data_insert = self.model().insert().values(kwargs)
            db.session.execute(data_insert)
            db.session.commit()

    def delete(self, **kwargs):
        with DBConnectionHandler() as db:
            filter_fields = self.__verify_filter_fields(**kwargs)
            db.session.query(self.model).filter(and_(*filter_fields)).delete()
            db.session.commit()

    def update(self, fields_and_new_values, **kwargs):
        if not isinstance(fields_and_new_values, dict):
            raise TypeError(
                f'A dict was expected for fields_and_new_values, but got an {type(fields_and_new_values).__name__}')

        if len(fields_and_new_values) == 0:
            raise ValueError('Argument passed to fields_and_new_values is empty')

        with DBConnectionHandler() as db:
            filter_fields = self.__verify_filter_fields(**kwargs)
            db.session.query(self.model).filter(and_(*filter_fields)).update(fields_and_new_values)
            db.session.commit()

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(self.model).all()

            return data

    def __verify_filter_fields(self, **kwargs):
        filter_fields = []

        for field, value in kwargs.items():
            try:
                hasattr(self.model, field)
            except AttributeError as e:
                raise e
            else:
                filter_fields.append(getattr(self.model, field) == value)

        return filter_fields