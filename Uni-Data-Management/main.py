"""Ranks students based on data"""
import os
from collections import OrderedDict
from decimal import Decimal

from pyexcel_ods import get_data


def get_academic_scores():
    """returns list of the academic scores for each student for each term"""
    scores = []
    for data_file in os.listdir("./data"):
        if data_file[:4] == "Data":
            data = get_data(f"data/{data_file}")
            data = list(data.items())[0][1][3:]
            scores += data

    return scores


def get_avg_scores(academic_scores):
    """returns dictionary of the average score for each student"""
    total_scores = {}
    for student in academic_scores:
        if student:
            # checks if the student has been added to the list of total scores
            if student[0] not in total_scores:
                total_scores[student[0]] = student[1:]
            else:
                for i in range(len(total_scores[student[0]])):
                    total_scores[student[0]][i] += student[i + 1]

    # multiply physics and algebra scores by 2
    for name in total_scores:
        total_scores[name][0] *= 2
        total_scores[name][1] *= 2

    # get dictionary of average scores
    avg_scores = {}
    for name, scores in total_scores.items():
        terms = 4
        avg_score = []
        for score in scores:
            avg_score.append(score / terms)

        avg_scores[name] = sum(avg_score) / len(avg_score)

    return avg_scores


def get_ielts_scores():
    """returns dictionary of ielts scores for each student"""
    ielts = get_data(f"data/IELTS.ods")
    ielts = list(ielts.items())[0][1][3:]
    ielts_scores = {}
    for student in ielts:
        ielts_scores[student[0]] = student[1:]

    for student in ielts_scores:
        scores = ielts_scores[student]

        # average of ielts scores are converted to percentage
        new_score = (sum(scores) / len(scores) / 9) * 100
        ielts_scores[student] = new_score

    return ielts_scores


def get_interview_scores():
    """returns dictionary of interview scores for each student"""
    interview_file = get_data(f"data/Interview.ods")
    interview_file = list(interview_file.items())[0][1][3:]
    interview_scores = {}
    for student in interview_file:
        interview_scores[student[0]] = student[1:]

    for student in interview_scores:
        scores = interview_scores[student]

        # average interview scores are converted to percentage
        new_score = (sum(scores) / len(scores) / 10) * 100
        interview_scores[student] = new_score

    return interview_scores


def get_overall_scores(academic_scores, ielts_scores, interview_scores):
    """return the final scores for each student"""
    overall_scores = {}
    for student in academic_scores:
        overall_scores[student] = Decimal(str(round(academic_scores[student] * 0.4, 2)))

    for student in ielts_scores:
        overall_scores[student] += Decimal(str(round(ielts_scores[student] * 0.3, 2)))

    for student in interview_scores:
        overall_scores[student] += Decimal(
            str(round(interview_scores[student] * 0.3, 2))
        )

    return overall_scores


def order_dict(dictionary):
    """Sorts the final scores by dictionary values"""
    sorted_values = sorted(dictionary.items(), key=lambda kv: kv[1])[::-1]

    new_dict = OrderedDict(sorted_values)

    return new_dict


def save_ranking(data):
    """Outputs ranking data to a txt file"""
    with open("ranking.txt", "w") as ranking:
        for rank, student in enumerate(data):
            ranking.write(f"{rank+1}. {student}: {data[student]}%\n")


def main():
    """main function"""
    overall_scores = {}

    student_academic_scores = get_academic_scores()
    avg_academic_scores = get_avg_scores(student_academic_scores)

    ielts_scores = get_ielts_scores()

    interview_scores = get_interview_scores()

    overall_scores = get_overall_scores(
        avg_academic_scores, ielts_scores, interview_scores
    )

    ranking = order_dict(overall_scores)

    save_ranking(ranking)
    print("Output stored in ranking.txt")


if __name__ == "__main__":
    main()
