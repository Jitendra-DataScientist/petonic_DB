select * from challenge_status;

delete from challenge_status where challenge_id=1;

UPDATE challenge_status
SET challenge_status = 'CC',
json_data = '{"UD": 1704181869.2065368}'
WHERE challenge_id = 1;

UPDATE challenge_status
SET challenge_status = 'CC',
    json_data = '{"UD": 1704181869.2065368,"UD": 1704181869.2065368}'
WHERE challenge_id = 1;
