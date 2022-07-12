from database.db import get_connection
from .entities.Team import Team


class TeamModel():

    @classmethod
    def get_teams(self):
        try:
            connection = get_connection()
            teams = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, role, released FROM team ORDER BY name ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    team = Team(row[0], row[1], row[2], row[3])
                    teams.append(team.to_JSON())

            connection.close()
            return teams
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_team(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, role, released FROM team WHERE id = %s", (id,))
                row = cursor.fetchone()

                team = None
                if row != None:
                    team = Team(row[0], row[1], row[2], row[3])
                    team = team.to_JSON()

            connection.close()
            return team
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_team(self, team):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO team (id, name, role, released) 
                                VALUES (%s, %s, %s, %s)""", (team.id, team.name, team.role, team.released))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_team(self, team):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE team SET name = %s, role = %s, released = %s 
                                WHERE id = %s""", (team., team.role, team.released, team.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_team(self, team):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM team WHERE id = %s", (team.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
