SELECT 
				Date(v.creation),
				v.modified_by as modified_mail,
				usr.full_name as modified_by, 
				v.docname,
				v.data,
				ccl.credit_limit
			FROM 
				`tabVersion` v
			LEFT JOIN 
				`tabUser` as usr on v.modified_by = usr.name
			LEFT JOIN 
				`tabCustomer Credit Limit` as ccl on v.docname = ccl.parent	
			WHERE 
				ref_doctype in ('Customer') 
				and DATE(v.creation) >= '2022-01-01' and  DATE(v.creation) <= '2022-12-31'
