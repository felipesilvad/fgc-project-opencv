import json

def parse_data(
  P1char1, P1char2, P1char3, P2char1, P2char2, P2char3,
  P1_round1_current_char, P2_round1_current_char, round1_P1_start_life, round1_P1_end_life, round1_P2_start_life, round1_P2_end_life,
  P1_round2_current_char, P2_round2_current_char, round2_P1_start_life, round2_P1_end_life, round2_P2_start_life, round2_P2_end_life,
  P1_round3_current_char, P2_round3_current_char, round3_P1_start_life, round3_P1_end_life, round3_P2_start_life, round3_P2_end_life,
  P1_round4_current_char, P2_round4_current_char, round4_P1_start_life, round4_P1_end_life, round4_P2_start_life, round4_P2_end_life,
  P1_round5_current_char, P2_round5_current_char, round5_P1_start_life, round5_P1_end_life, round5_P2_start_life, round5_P2_end_life,
  ):
  data = {
    "id": [
        {
            "P1char1": P1char1,
            "P1char2": P1char2,
            "P1char3": P1char3,
            "P2char1": P2char1,
            "P2char2": P2char2,
            "P2char3": P2char3,
            "round1": {
              "P1char": P1_round1_current_char,
              "P2char": P2_round1_current_char,
              "P1_StartLife": round1_P1_start_life,
              "P1_EndLife": round1_P1_end_life,
              "P2_StartLife": round1_P2_start_life,
              "P2_EndLife": round1_P2_end_life,
            },
            "round2": {
              "P1char": P1_round2_current_char,
              "P2char": P2_round2_current_char,
              "P1_StartLife": round2_P1_start_life,
              "P1_EndLife": round2_P1_end_life,
              "P2_StartLife": round2_P2_start_life,
              "P2_EndLife": round2_P2_end_life,
            },
            "round3": {
              "P1char": P1_round3_current_char,
              "P2char": P2_round3_current_char,
              "P1_StartLife": round3_P1_start_life,
              "P1_EndLife": round3_P1_end_life,
              "P2_StartLife": round3_P2_start_life,
              "P2_EndLife": round3_P2_end_life,
            },
            "round4": {
              "P1char": P1_round4_current_char,
              "P2char": P2_round4_current_char,
              "P1_StartLife": round4_P1_start_life,
              "P1_EndLife": round4_P1_end_life,
              "P2_StartLife": round4_P2_start_life,
              "P2_EndLife": round4_P2_end_life,
            },
            "round5": {
              "P1char": P1_round5_current_char,
              "P2char": P2_round5_current_char,
              "P1_StartLife": round5_P1_start_life,
              "P1_EndLife": round5_P1_end_life,
              "P2_StartLife": round5_P2_start_life,
              "P2_EndLife": round5_P2_end_life,
            },
        }
    ]
  }
  return data

def write_json(data, filename="jsons/test.json"):
  with open(filename, "w") as f:
    json.dump(data, f,  indent=4)

  write_json(data)