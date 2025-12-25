# Assessment Evaluation Guide

## Overview
This document describes the evaluation methodology for the Molding Assessment system. The assessments evaluate the knowledge and skills of operators in injection molding processes through multiple-choice questions across different difficulty levels.

## Assessment Structure

### Master Data (JSON)
These files contain the "source of truth", including questions, correct answers, reasoning, and scoring values. They are used for automated processing and API synchronization.
- `master_assesment/json/basic_assesment.json`: Basic level master data.
- `master_assesment/json/medium_assesment.json`: Medium level master data.
- `master_assesment/json/advanced_assesment.json`: Advanced level master data.

### Study Guides (Markdown)
Clean versions of the assessments intended for study or manual review. They include the questions and options but **exclude** the correct answers and reasoning.
- `docs/questions/LEVEL_1_BASIC_ASSESSMENT.md`: Basic Level Guide.
- `docs/questions/LEVEL_2_MEDIUM_ASSESSMENT.md`: Medium Level Guide.
- `docs/questions/LEVEL_3_ADVANCED_ASSESSMENT.md`: Advanced Level Guide.

### Question Categories
- Máquina (Machine)
- Plásticos (Plastics)
- Seguridad (Safety)
- Molde (Mold)
- Calidad (Quality)
- Operaciones (Operations)
- Desperdicios (Waste)
- Procesos (Processes)

### Question Types
- Teórico: Theoretical knowledge
- Práctico: Practical application

## Scoring Method

### Individual Question Scoring (est_score)
Each question has an `est_score` value based on difficulty:

| Level | Theoretical | Practical |
|-------|-------------|-----------|
| Basic | 1.0 | 1.5 |
| Medium | 2.0 | 2.5 |
| Advanced | 3.0 | 3.5 |

- **Theoretical**: Knowledge-based questions
- **Practical**: Application-oriented questions requiring problem-solving

### Total Score Calculation
The total score for an assessment is the sum of `est_score` values for correctly answered questions.

**Formula:**
```
Total Score = Σ(est_score of correct answers)
```

### Maximum Possible Scores
- Basic: 50 questions × average ~1.25 = ~62.5 points
- Medium: 60 questions × average ~2.25 = ~135 points
- Advanced: 60 questions × average ~3.25 = ~195 points

## Evaluation Process

1. **Question Presentation**: Questions are presented in randomized order to prevent cheating.

2. **Answer Selection**: User selects one answer from three options.

3. **Immediate Feedback**: Show correct answer and reasoning after each question.

4. **Score Accumulation**: Add `est_score` to total only if answer is correct.

5. **Final Report**: Display total score, percentage correct, and breakdown by category.

## Weighting Rationale
- **Difficulty Levels**: Higher scores for advanced questions reflect greater expertise required.
- **Type Adjustment**: Practical questions receive +0.5 points as they test real-world application, considered slightly harder than theoretical knowledge.
- **Expert Determination**: Scores assigned based on subject matter expert analysis of question complexity and operator skill requirements.

## Data Processing for Data Scientists

### Data Format
Each assessment file is a JSON array of question objects:

```json
{
  "id": "unique_question_id",
  "categoria": "Category",
  "tipo": "Teórico|Práctico",
  "pregunta": "Question text",
  "respuestas": ["Option A", "Option B", "Option C"],
  "respuesta_correcta": "Correct Option",
  "razonamiento": "Explanation",
  "est_score": 1.0
}
```

### Processing Workflow

1. **Load Assessment Data**
   ```python
   import json
   with open('basic_assesment.json', 'r') as f:
       questions = json.load(f)
   ```

2. **User Response Collection**
   - Collect user answers as list of selected options
   - Match against `respuesta_correcta`

3. **Score Calculation**
   ```python
   def calculate_score(questions, user_answers):
       total_score = 0
       correct_count = 0
       for i, q in enumerate(questions):
           if user_answers[i] == q['respuesta_correcta']:
               total_score += q['est_score']
               correct_count += 1
       return total_score, correct_count
   ```

4. **Analytics Data Structure**
   ```python
   result = {
       'user_id': 'user123',
       'assessment_level': 'basic',
       'total_score': 45.5,
       'max_score': 62.5,
       'percentage': 72.8,
       'correct_answers': 35,
       'total_questions': 50,
       'category_breakdown': {
           'Máquina': {'correct': 5, 'total': 7, 'score': 6.5},
           'Plásticos': {'correct': 4, 'total': 6, 'score': 5.0},
           # ... other categories
       },
       'timestamp': '2024-12-25T12:00:00Z'
   }
   ```

5. **Key Metrics for Analysis**
   - Overall competency score
   - Category-specific strengths/weaknesses
   - Theoretical vs Practical performance
   - Learning progress over time

### Database Schema Suggestion
```sql
CREATE TABLE assessment_results (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255),
    assessment_level VARCHAR(50),
    total_score DECIMAL(5,2),
    max_score DECIMAL(5,2),
    percentage DECIMAL(5,2),
    correct_answers INT,
    total_questions INT,
    category_breakdown JSONB,
    completed_at TIMESTAMP
);
```

This scoring system ensures fair evaluation while allowing data scientists to perform detailed analytics on operator performance and training effectiveness.