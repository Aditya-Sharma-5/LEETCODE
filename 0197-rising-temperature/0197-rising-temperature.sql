# Write your MySQL query statement below
# select w2.id from Weather w1 , Weather w2 WHERE w2.recordDate -1 = w1.recordDate and w2.temperature > w1.temperature;


SELECT w2.id FROM Weather w1, Weather w2
WHERE w1.recordDate = (w2.recordDate - INTERVAL 1 DAY) AND w1.Temperature < w2.Temperature