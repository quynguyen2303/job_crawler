import requests
import json

def fetch_topdev_data(page_number):
    url = f'https://api.topdev.vn/td/v2/jobs?fields[job]=id,title,salary,company,extra_skills,skills_str,skills_arr,skills_ids,job_types_str,job_levels_str,job_levels_arr,job_levels_ids,addresses,status_display,detail_url,job_url,salary,published,refreshed,applied,candidate,requirements_arr,packages,benefits,content,features,is_free,is_basic,is_basic_plus,is_distinction&fields[company]=tagline,addresses,skills_arr,industries_arr,industries_str,image_cover,image_galleries,benefits&page={page_number}&locale=vi_VN'

    response = requests.get(url)
    data = response.json()['data']
    
    job_title = []
    company = []
    job_description = []
    company_logo = []
    company_detail_url = []
    sorted_addresses = []
    industries_str = []
    job_types_str = []
    job_levels_str = []
    detail_url = []
    published_date = []
    
    for item in data:
        job_title.append(item['title'])
        company.append(item['company']['display_name'])
        job_description.append(item['content'])
        company_logo.append(item['company']['image_logo'])
        company_detail_url.append(item['company']['detail_url'])
        sorted_addresses.append(item['company']['addresses']['sort_addresses'])
        industries_str.append(item['company']['industries_str'])
        job_types_str.append(item['job_types_str'])
        job_levels_str.append(item['job_levels_str'])
        detail_url.append(item['detail_url'])
        published_date.append(item['published']['date'])
    
    return (
        job_title,
        company,
        job_description,
        company_logo,
        company_detail_url,
        sorted_addresses,
        industries_str,
        job_types_str,
        job_levels_str,
        detail_url,
        published_date
    )

all_job_title = []
all_company = []
all_job_description = []
all_company_logo = []
all_company_detail_url = []
all_sorted_addresses = []
all_industries_str = []
all_job_types_str = []
all_job_levels_str = []
all_detail_url = []
all_published_date = []

for page_number in range(1, 101):
    (
        job_title,
        company,
        job_description,
        company_logo,
        company_detail_url,
        sorted_addresses,
        industries_str,
        job_types_str,
        job_levels_str,
        detail_url,
        published_date
    ) = fetch_topdev_data(page_number)
    
    all_job_title.extend(job_title)
    all_company.extend(company)
    all_job_description.extend(job_description)
    all_company_logo.extend(company_logo)
    all_company_detail_url.extend(company_detail_url)
    all_sorted_addresses.extend(sorted_addresses)
    all_industries_str.extend(industries_str)
    all_job_types_str.extend(job_types_str)
    all_job_levels_str.extend(job_levels_str)
    all_detail_url.extend(detail_url)
    all_published_date.extend(published_date)

with open('topdev.json', 'w') as file:
    json.dump({
        'job_title': all_job_title,
        'company': all_company,
        'job_description': all_job_description,
        'company_logo': all_company_logo,
        'company_detail_url': all_company_detail_url,
        'sorted_addresses': all_sorted_addresses,
        'industries_str': all_industries_str,
        'job_types_str': all_job_types_str,
        'job_levels_str': all_job_levels_str,
        'detail_url': all_detail_url,
        'published_date': all_published_date
    }, file)


'''
sample_json = {
      "id": 2031735,
      "title": "Web Developer (HTML, CSS, JavaScript)",
      "content": "<ul style=\"color: #212529;\">\r\n<li style=\"text-align: justify;\"><span style=\"font-family: Roboto, Helvetica, Verdana, Arial, sans-serif; font-size: 15px; color: #393e46;\">Đối với ứng vi&ecirc;n mới ra trường: Mức lương cơ bản từ 9.000.000 VNĐ trở l&ecirc;n v&agrave; được hỗ trợ training.</span></li>\r\n<li style=\"text-align: justify;\"><span style=\"font-family: Roboto, Helvetica, Verdana, Arial, sans-serif; font-size: 15px; color: #393e46;\">Đối với ứng vi&ecirc;n c&oacute; kinh nghiệm từ 1 năm trở l&ecirc;n (ưu thế về lĩnh vực viễn th&ocirc;ng): Thu nhập từ 12.000.000 - 25.000.000 VNĐ, trao đổi th&ecirc;m khi phỏng vấn.</span></li>\r\n</ul>",
      "benefits": [],
      "owned_id": 72403,
      "company": {
        "id": 72403,
        "display_name": "South Telecom",
        "image_logo": "https://assets.topdev.vn/images/2020/07/22/logonHXVEqXDWg7m3totbQkEf1JOyXdv92j5-dErSQ.png",
        "slug": "south-telecom",
        "detail_url": "https://topdev.vn/nha-tuyen-dung/south-telecom-72403",
        "tagline": "Nhà cung cấp dịch vụ số - DSP (Digital Service Provider)",
        "addresses": {
          "address_region_ids": [
            "79",
            "01",
            "79"
          ],
          "address_region_list": "Thành phố Hồ Chí Minh, Thành phố Hà Nội, Thành phố Hồ Chí Minh",
          "address_region_array": [
            "Thành phố Hồ Chí Minh",
            "Thành phố Hà Nội",
            "Thành phố Hồ Chí Minh"
          ],
          "full_addresses": [
            "Head Office: ST Group - 136/12 Vườn Chuối, Phường 04, Quận 3, Thành phố Hồ Chí Minh",
            "Ha Noi Office: ST Building - Số 3, Ngõ 18, Đường Yên Lãng, Phường Láng Hạ, Quận Đống Đa, Thành phố Hà Nội",
            "Đường Điện Biên Phủ, Phường 04, Quận 3, Thành phố Hồ Chí Minh"
          ],
          "sort_addresses": "Quận 3, Hồ Chí Minh - Quận Đống Đa, Hà Nội - Quận 3, Hồ Chí Minh",
          "collection_addresses": [
            {
              "id": 33244,
              "ward": {
                "id": "27148",
                "value": "Phường 04"
              },
              "province": {
                "id": "79",
                "value": "Thành phố Hồ Chí Minh"
              },
              "district": {
                "id": "770",
                "value": "Quận 3"
              },
              "postal_code": "700000",
              "full_address": "Head Office: ST Group - 136/12 Vườn Chuối, Phường 04, Quận 3, Thành phố Hồ Chí Minh",
              "latitude": null,
              "longitude": null,
              "street": "Head Office: ST Group - 136/12 Vườn Chuối"
            },
            {
              "id": 135444,
              "ward": {
                "id": "00199",
                "value": "Phường Láng Hạ"
              },
              "province": {
                "id": "01",
                "value": "Thành phố Hà Nội"
              },
              "district": {
                "id": "006",
                "value": "Quận Đống Đa"
              },
              "postal_code": "100000",
              "full_address": "Ha Noi Office: ST Building - Số 3, Ngõ 18, Đường Yên Lãng, Phường Láng Hạ, Quận Đống Đa, Thành phố Hà Nội",
              "latitude": null,
              "longitude": null,
              "street": "Ha Noi Office: ST Building - Số 3, Ngõ 18, Đường Yên Lãng"
            },
            {
              "id": 175817,
              "ward": {
                "id": "27148",
                "value": "Phường 04"
              },
              "province": {
                "id": "79",
                "value": "Thành phố Hồ Chí Minh"
              },
              "district": {
                "id": "770",
                "value": "Quận 3"
              },
              "postal_code": "700000",
              "full_address": "Đường Điện Biên Phủ, Phường 04, Quận 3, Thành phố Hồ Chí Minh",
              "latitude": null,
              "longitude": null,
              "street": "Đường Điện Biên Phủ"
            }
          ],
          "address_short_region_list": "Hồ Chí Minh, Hà Nội, Hồ Chí Minh"
        },
        "image_cover": "https://assets.topdev.vn/images/2022/08/10/TopDev-f438eebea0bb2ca0ae8ed3240d1eb627-1660101920.jpg",
        "image_galleries": [
          {
            "id": 260819,
            "url": "https://assets.topdev.vn/images/2021/04/15/086c3dd532943f75303e2845eb379e9f-z46WA.jpeg",
            "path": "/images/2021/04/15/086c3dd532943f75303e2845eb379e9f-z46WA.jpeg",
            "name": "086c3dd532943f75303e2845eb379e9f.jpeg",
            "uploaded": {
              "date": "15-04-2021",
              "datetime": "2021-04-15 10:57:49",
              "since": "2 years ago",
              "timestamp": 1618459069
            },
            "source": "Unknown"
          },
          {
            "id": 260820,
            "url": "https://assets.topdev.vn/images/2021/04/15/6ef44e9fa65ccbdaaa19b71411fa457e-CBbEV.jpeg",
            "path": "/images/2021/04/15/6ef44e9fa65ccbdaaa19b71411fa457e-CBbEV.jpeg",
            "name": "6ef44e9fa65ccbdaaa19b71411fa457e.jpeg",
            "uploaded": {
              "date": "15-04-2021",
              "datetime": "2021-04-15 10:57:49",
              "since": "2 years ago",
              "timestamp": 1618459069
            },
            "source": "Unknown"
          },
          {
            "id": 260822,
            "url": "https://assets.topdev.vn/images/2021/04/15/a1a46eae7f2eeaff766117d3418abb54-j7e0V.jpg",
            "path": "/images/2021/04/15/a1a46eae7f2eeaff766117d3418abb54-j7e0V.jpg",
            "name": "a1a46eae7f2eeaff766117d3418abb54.jpg",
            "uploaded": {
              "date": "15-04-2021",
              "datetime": "2021-04-15 10:57:49",
              "since": "2 years ago",
              "timestamp": 1618459069
            },
            "source": "Unknown"
          },
          {
            "id": 260823,
            "url": "https://assets.topdev.vn/images/2021/04/15/05c5449b16924eb42512a1d177f80a9a-PovYd.jpeg",
            "path": "/images/2021/04/15/05c5449b16924eb42512a1d177f80a9a-PovYd.jpeg",
            "name": "05c5449b16924eb42512a1d177f80a9a.jpeg",
            "uploaded": {
              "date": "15-04-2021",
              "datetime": "2021-04-15 10:57:49",
              "since": "2 years ago",
              "timestamp": 1618459069
            },
            "source": "Unknown"
          },
          {
            "id": 337143,
            "url": "https://assets.topdev.vn/images/2022/06/27/TopDev-IMG3206-1656322234.JPG",
            "path": "/images/2022/06/27/TopDev-IMG3206-1656322234.JPG",
            "name": "IMG_3206.JPG",
            "uploaded": {
              "date": "27-06-2022",
              "datetime": "2022-06-27 16:30:34",
              "since": "1 year ago",
              "timestamp": 1656322234
            },
            "source": "Unknown"
          },
          {
            "id": 337144,
            "url": "https://assets.topdev.vn/images/2022/06/27/TopDev-IMG3524-1656322234.JPG",
            "path": "/images/2022/06/27/TopDev-IMG3524-1656322234.JPG",
            "name": "IMG_3524.JPG",
            "uploaded": {
              "date": "27-06-2022",
              "datetime": "2022-06-27 16:30:34",
              "since": "1 year ago",
              "timestamp": 1656322234
            },
            "source": "Unknown"
          },
          {
            "id": 346115,
            "url": "https://assets.topdev.vn/images/2022/08/10/TopDev-1f50ab5e9111a6f987926c7e85cc530e-1660101921.jpg",
            "path": "/images/2022/08/10/TopDev-1f50ab5e9111a6f987926c7e85cc530e-1660101921.jpg",
            "name": "1f50ab5e9111a6f987926c7e85cc530e.jpg",
            "uploaded": {
              "date": "10-08-2022",
              "datetime": "2022-08-10 10:25:21",
              "since": "1 year ago",
              "timestamp": 1660101921
            },
            "source": "Unknown"
          },
          {
            "id": 346123,
            "url": "https://assets.topdev.vn/images/2022/08/10/TopDev-SouthTelecom-image-1-1660102801.jpg",
            "path": "/images/2022/08/10/TopDev-SouthTelecom-image-1-1660102801.jpg",
            "name": "South Telecom-image-1.jpg",
            "uploaded": {
              "date": "10-08-2022",
              "datetime": "2022-08-10 10:40:01",
              "since": "1 year ago",
              "timestamp": 1660102801
            },
            "source": "Unknown"
          },
          {
            "id": 346124,
            "url": "https://assets.topdev.vn/images/2022/08/10/TopDev-SouthTelecom-image-2-1660102801.jpg",
            "path": "/images/2022/08/10/TopDev-SouthTelecom-image-2-1660102801.jpg",
            "name": "South Telecom-image-2.jpg",
            "uploaded": {
              "date": "10-08-2022",
              "datetime": "2022-08-10 10:40:01",
              "since": "1 year ago",
              "timestamp": 1660102801
            },
            "source": "Unknown"
          }
        ],
        "benefits": [
          {
            "value": "Bonus: 13th-14th month salary & Performance bonus.",
            "icon": "fa-dollar"
          },
          {
            "value": "Health and Social insurance.",
            "icon": "fa-user-md"
          },
          {
            "value": "Annual Health Checkup",
            "icon": "fa-heartbeat"
          },
          {
            "value": "Team building, Event, Company trip.",
            "icon": "fa-plane"
          },
          {
            "value": "Time working: from Monday to Friday.",
            "icon": "fa-calendar-check-o"
          }
        ],
        "skills_arr": [
          "PHP",
          "Agile",
          "Java",
          ".NET",
          "HTML",
          "LESS",
          "SASS"
        ],
        "industries_arr": [
          "Dịch vụ IT",
          "Internet"
        ],
        "industries_str": "Dịch vụ IT, Internet",
        "is_followed": false
      },
      "extra_skills": [],
      "skills_str": "CSS, JavaScript, HTML",
      "skills_arr": [
        "CSS",
        "JavaScript",
        "HTML"
      ],
      "skills_ids": [
        3,
        22,
        75
      ],
      "job_types_str": "",
      "job_levels_str": "Fresher, Junior",
      "job_levels_arr": [
        "Fresher",
        "Junior"
      ],
      "job_levels_ids": [
        1617,
        8664
      ],
      "addresses": {
        "address_region_ids": [
          "79"
        ],
        "address_region_list": "Thành phố Hồ Chí Minh",
        "address_region_array": [
          "Thành phố Hồ Chí Minh"
        ],
        "full_addresses": [
          "Head Office: ST Group - 136/12 Vườn Chuối, Phường 04, Quận 3, Thành phố Hồ Chí Minh"
        ],
        "sort_addresses": "Quận 3, Hồ Chí Minh",
        "collection_addresses": [
          {
            "id": 33244,
            "ward": {
              "id": "27148",
              "value": "Phường 04"
            },
            "province": {
              "id": "79",
              "value": "Thành phố Hồ Chí Minh"
            },
            "district": {
              "id": "770",
              "value": "Quận 3"
            },
            "postal_code": "700000",
            "full_address": "Head Office: ST Group - 136/12 Vườn Chuối, Phường 04, Quận 3, Thành phố Hồ Chí Minh",
            "latitude": null,
            "longitude": null,
            "street": "Head Office: ST Group - 136/12 Vườn Chuối"
          }
        ]
      },
      "status_display": "Open",
      "detail_url": "https://topdev.vn/viec-lam/web-developer-html-css-javascript-south-telecom-2031735",
      "job_url": "",
      "salary": {
        "is_negotiable": 0,
        "unit": "MONTH",
        "min": "9******",
        "max": "2*******",
        "currency": "VND",
        "min_estimate": 0,
        "max_estimate": 0,
        "currency_estimate": "VND",
        "value": "9****** - 2******* VND"
      },
      "features": [
        "FresherPage"
      ],
      "packages": [
        "basic-plus"
      ],
      "is_free": false,
      "is_basic": false,
      "is_basic_plus": true,
      "is_distinction": false,
      "is_salary_visible": false,
      "published": {
        "date": "09-10-2023",
        "datetime": "00:00:00 09-10-2023",
        "since": "1 ngày trước"
      },
      "refreshed": {
        "date": "09-10-2023",
        "datetime": "09:44:28 09-10-2023",
        "since": "1 ngày trước"
      },
      "applied": null,
      "candidate": null,
      "is_applied": false,
      "is_followed": false,
      "is_blacklisted": false,
      "recalled_at": null,
      "is_remove_cv": false,
      "is_viewed": false,
      "requirements_arr": [
        {
          "value": [
            "Chấp nhận Fresher hoặc có ít nhất 01 năm kinh nghiệm.",
            "Thành thạo HTML, CSS, và ngôn ngữ lập trình Javascript.",
            "Có kinh nghiệm sử dụng ES6, ES7, ReactJS, Redux, Redux-Saga, CSS Compiler (Scss/Less).",
            "Có khả năng sử dụng Git.",
            "Có kiến thức về lập trình hướng đối tượng (OOP) và design pattern.",
            "Có kiến thức về Responsive Web Design, RESTful APIs.",
            "Có kinh nghiệm sử dụng các Front-End Development tools phổ biến như Babel, Webpack, NPM, etc.",
            "Có khả năng tư duy tốt.",
            "Hiểu biết về SEO, NextJS, NodeJS, MongoDB, React Native là một điểm cộng."
          ],
          "icon": "fa-circle"
        }
      ]
}
'''
