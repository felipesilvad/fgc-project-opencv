import json

def parse_round_data(P1char1, P1char2, P1char3, P2char1, P2char2, P2char3, rounds, winner, loser, 
round1_time, round2_time, round3_time, round4_time, round5_time):
  if len(rounds) == 3:
    data = {
      "P1char1": P1char1, "P1char2": P1char2, "P1char3": P1char3, "P2char1": P2char1, "P2char2": P2char2, "P2char3": P2char3,
      "winner": winner, "loser": loser,
      "round1": {
        'time': round1_time,
        'P1_current_char': rounds[0][0], 'P2_current_char': rounds[0][1],
        'P1_start_life': rounds[0][2], 'P1_end_life': rounds[0][3], 'P1_damage_taken': int(rounds[0][2]) - int(rounds[0][3]),
        'P2_start_life': rounds[0][4], 'P2_end_life': rounds[0][5], 'P2_damage_taken': int(rounds[0][4]) - int(rounds[0][5]),
      },
      "round2": {
        'time': round2_time,
        'P1_current_char': rounds[1][0], 'P2_current_char': rounds[1][1],
        'P1_start_life': rounds[1][2], 'P1_end_life': rounds[1][3], 'P1_damage_taken': int(rounds[1][2]) - int(rounds[1][3]),
        'P2_start_life': rounds[1][4], 'P2_end_life': rounds[1][5], 'P2_damage_taken': int(rounds[1][4]) - int(rounds[1][5]),
      },
      "round3": {
        'time': round3_time,
        'P1_current_char': rounds[2][0], 'P2_current_char': rounds[2][1],
        'P1_start_life': rounds[2][2], 'P1_end_life': rounds[2][3], 'P1_damage_taken': int(rounds[2][2]) - int(rounds[2][3]),
        'P2_start_life': rounds[2][4], 'P2_end_life': rounds[2][5], 'P2_damage_taken': int(rounds[2][4]) - int(rounds[2][5]),
      },
    }
  if len(rounds) == 4:
    data = {
      "P1char1": P1char1, "P1char2": P1char2, "P1char3": P1char3, "P2char1": P2char1, "P2char2": P2char2, "P2char3": P2char3,
      "winner": winner, "loser": loser,
      "round1": {
        'time': round1_time,
        'P1_current_char': rounds[0][0], 'P2_current_char': rounds[0][1],
        'P1_start_life': rounds[0][2], 'P1_end_life': rounds[0][3], 'P1_damage_taken': int(rounds[0][2]) - int(rounds[0][3]),
        'P2_start_life': rounds[0][4], 'P2_end_life': rounds[0][5], 'P2_damage_taken': int(rounds[0][4]) - int(rounds[0][5]),
      },
      "round2": {
        'time': round2_time,
        'P1_current_char': rounds[1][0], 'P2_current_char': rounds[1][1],
        'P1_start_life': rounds[1][2], 'P1_end_life': rounds[1][3], 'P1_damage_taken': int(rounds[1][2]) - int(rounds[1][3]),
        'P2_start_life': rounds[1][4], 'P2_end_life': rounds[1][5], 'P2_damage_taken': int(rounds[1][4]) - int(rounds[1][5]),
      },
      "round3": {
        'time': round3_time,
        'P1_current_char': rounds[2][0], 'P2_current_char': rounds[2][1],
        'P1_start_life': rounds[2][2], 'P1_end_life': rounds[2][3], 'P1_damage_taken': int(rounds[2][2]) - int(rounds[2][3]),
        'P2_start_life': rounds[2][4], 'P2_end_life': rounds[2][5], 'P2_damage_taken': int(rounds[2][4]) - int(rounds[2][5]),
      },
      "round4": {
        'time': round4_time,
        'P1_current_char': rounds[3][0], 'P2_current_char': rounds[3][1],
        'P1_start_life': rounds[3][2], 'P1_end_life': rounds[3][3], 'P1_damage_taken': int(rounds[3][2]) - int(rounds[3][3]),
        'P2_start_life': rounds[3][4], 'P2_end_life': rounds[3][5], 'P2_damage_taken': int(rounds[3][4]) - int(rounds[3][5]),
      },
    }
  if len(rounds) == 5:
    data = {
      "P1char1": P1char1, "P1char2": P1char2, "P1char3": P1char3, "P2char1": P2char1, "P2char2": P2char2, "P2char3": P2char3,
      "winner": winner, "loser": loser,
      "round1": {
        'time': round1_time,
        'P1_current_char': rounds[0][0], 'P2_current_char': rounds[0][1],
        'P1_start_life': rounds[0][2], 'P1_end_life': rounds[0][3], 'P1_damage_taken': int(rounds[0][2]) - int(rounds[0][3]),
        'P2_start_life': rounds[0][4], 'P2_end_life': rounds[0][5], 'P2_damage_taken': int(rounds[0][4]) - int(rounds[0][5]),
      },
      "round2": {
        'time': round2_time,
        'P1_current_char': rounds[1][0], 'P2_current_char': rounds[1][1],
        'P1_start_life': rounds[1][2], 'P1_end_life': rounds[1][3], 'P1_damage_taken': int(rounds[1][2]) - int(rounds[1][3]),
        'P2_start_life': rounds[1][4], 'P2_end_life': rounds[1][5], 'P2_damage_taken': int(rounds[1][4]) - int(rounds[1][5]),
      },
      "round3": {
        'time': round3_time,
        'P1_current_char': rounds[2][0], 'P2_current_char': rounds[2][1],
        'P1_start_life': rounds[2][2], 'P1_end_life': rounds[2][3], 'P1_damage_taken': int(rounds[2][2]) - int(rounds[2][3]),
        'P2_start_life': rounds[2][4], 'P2_end_life': rounds[2][5], 'P2_damage_taken': int(rounds[2][4]) - int(rounds[2][5]),
      },
      "round4": {
        'time': round4_time,
        'P1_current_char': rounds[3][0], 'P2_current_char': rounds[3][1],
        'P1_start_life': rounds[3][2], 'P1_end_life': rounds[3][3], 'P1_damage_taken': int(rounds[3][2]) - int(rounds[3][3]),
        'P2_start_life': rounds[3][4], 'P2_end_life': rounds[3][5], 'P2_damage_taken': int(rounds[3][4]) - int(rounds[3][5]),
      },
      "round5": {
        'time': round5_time,
        'P1_current_char': rounds[4][0], 'P2_current_char': rounds[4][1],
        'P1_start_life': rounds[4][2], 'P1_end_life': rounds[4][3], 'P1_damage_taken': int(rounds[4][2]) - int(rounds[4][3]),
        'P2_start_life': rounds[4][4], 'P2_end_life': rounds[4][5], 'P2_damage_taken': int(rounds[4][4]) - int(rounds[4][5]),
      },
    }
  return data

def parse_game_data(id, player1, player2, date, tournament_id, type, video_id,
  games_count, game1_data, game2_data, game3_data, game4_data, game5_data
  ):
  if games_count >= 2:
    data = {
      f"{id}": {
        "player1": player1,
        "player2": player2,
        "date": date,
        "tournament_id": tournament_id,
        "type": type,
        "video_id": video_id,
        "game1": game1_data,
        "game2": game2_data,
      }
    }
  if games_count >= 3:
    data = {
      f"{id}": {
        "player1": player1,
        "player2": player2,
        "date": date,
        "tournament_id": tournament_id,
        "type": type,
        "video_id": video_id,
        "game1": game1_data,
        "game2": game2_data,
        "game3": game3_data,
      }
    }
  if games_count >= 4:
    data = {
      f"{id}": {
        "player1": player1,
        "player2": player2,
        "date": date,
        "tournament_id": tournament_id,
        "type": type,
        "video_id": video_id,
        "game1": game1_data,
        "game2": game2_data,
        "game3": game3_data,
        "game4": game4_data,
      }
    }
  if games_count >= 5:
    data = {
      f"{id}": {
        "player1": player1,
        "player2": player2,
        "date": date,
        "tournament_id": tournament_id,
        "type": type,
        "video_id": video_id,
        "game1": game1_data,
        "game2": game2_data,
        "game3": game3_data,
        "game4": game4_data,
        "game5": game5_data,
      }
    }
  return data

def write_json(data, filename):
  with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)