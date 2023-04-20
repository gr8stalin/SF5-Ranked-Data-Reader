import openpyxl
from datatypes import RankedMatch, RankedSession, GameResult


def parse_data_from_workbook():
    ranked_data_workbook = openpyxl.load_workbook("/home/gr8stalin/Documents/jiveGrind.xlsx")
    sheets = [x for x in ranked_data_workbook.sheetnames if "New" not in x]
    sessions = []

    for sheet in sheets:
        worksheet = ranked_data_workbook[sheet]
        points_start = int(worksheet["F2"].value)
        points_end = int(worksheet["G2"].value)
        matches = []
        for row in worksheet.iter_rows(min_row=2, max_col=4, values_only=True):
            if any(row):
                points = int(row[0])
                result = GameResult.from_str(row[1])
                opponent = row[2]
                replay_id = row[3]
                current_match = RankedMatch(points, result, opponent, replay_id)
                matches.append(current_match)
        current_session = RankedSession(points_start, points_end, matches)
        sessions.append(current_session)
    return sessions


if __name__ == '__main__':
    all_ranked_sessions = parse_data_from_workbook()
    print("done")
