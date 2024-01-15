select * from industry_list;

select * from domain_list;

select * from process_list;

delete from industry_list;

delete from domain_list;

delete from process_list;

select * from industry_domain_process_key_factors;

select key_factor, suggested_values, description
from industry_domain_process_key_factors
where industry = 'Environmental and Sustainability'
and domain = 'Environmental Impact Assessment'
and process = 'Screening';

delete from industry_domain_process_key_factors;

drop table score_params;