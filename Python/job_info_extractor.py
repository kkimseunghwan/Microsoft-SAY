from bs4 import BeautifulSoup

def extract_job_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 경력 정보 추출
    experience = soup.find('dt', string='경력').find_next('dd').text.strip()
    
    # 근무지역 정보 추출
    location = soup.find('dt', string='근무지역').find_next('dd').find('li').text.strip()
    
    return {
        '경력': experience,
        '근무지역': location
    }

# 사용 예시
html_content = """
<div class="sc-b12ae455-0 ehVsnD">
    <h2 class="blind">포지션 경력/학력/마감일/근무지역 정보</h2>
    <dl class="sc-b12ae455-1 hvXrQd">
        <dt>경력</dt>
        <dd>경력 9~20년</dd>
    </dl>
    <dl class="sc-b12ae455-1 hvXrQd">
        <dt>학력</dt>
        <dd>대학교졸업(4년) 이상</dd>
    </dl>
    <dl class="sc-b12ae455-1 hvXrQd">
        <dt>마감일</dt>
        <dd>2025-05-20</dd>
    </dl>
    <dl class="sc-b12ae455-1 hvXrQd">
        <dt>근무지역</dt>
        <dd>
            <ul>
                <li>경기 용인시 수지구 신수로 767 분당수지유타워 A동 1411호</li>
            </ul>
        </dd>
    </dl>
</div>
"""

job_info = extract_job_info(html_content)
print("추출된 정보:")
print(f"경력: {job_info['경력']}")
print(f"근무지역: {job_info['근무지역']}") 