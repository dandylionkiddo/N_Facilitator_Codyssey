import sys

# 1. 기본 데이터 설정 (이전 미션 샘플 3개 포함)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝고 화사한 배경에 제품이 중앙에 위치해야 합니다.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 20년 경력의 IT 컨설턴트입니다. 기술적인 용어를 쉽게 풀어서 설명하고 비즈니스 관점에서 조언해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]

categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    return input("선택: ")

def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ").strip()
    content = input("내용: ").strip()
    
    if not title or not content:
        print("❌ 오류: 제목과 내용은 비어있을 수 없습니다.")
        return

    print("\n카테고리 선택:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")
    
    try:
        cat_choice = int(input("선택: "))
        if 1 <= cat_choice <= len(categories):
            category = categories[cat_choice - 1]
        else:
            category = "기타"
    except ValueError:
        category = "기타"

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)
    print("\n✅ 프롬프트가 추가되었습니다!")

def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, 1):
        fav_star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{fav_star}")
    
    print(f"\n총 {len(prompts)}개의 프롬프트")

def view_by_category():
    print("\n=== 카테고리별 조회 ===")
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")
    
    try:
        choice = int(input("선택: "))
        if 1 <= choice <= len(categories):
            selected_cat = categories[choice - 1]
        else:
            print("❌ 잘못된 선택입니다.")
            return
        
        filtered = [p for p in prompts if p["category"] == selected_cat]
        
        print(f"\n[{selected_cat}] 카테고리 프롬프트:")
        if not filtered:
            print("해당 카테고리에 프롬프트가 없습니다.")
        else:
            for i, p in enumerate(filtered, 1):
                fav_star = " ⭐" if p["favorite"] else ""
                print(f"{i}. {p['title']}{fav_star}")
            print(f"\n총 {len(filtered)}개의 프롬프트")
    except ValueError:
        print("❌ 숫자만 입력 가능합니다.")

def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]
    
    print("\n검색 결과:")
    if not results:
        print("검색 결과가 없습니다.")
    else:
        for i, p in enumerate(results, 1):
            fav_star = " ⭐" if p["favorite"] else ""
            print(f"{i}. [{p['category']}] {p['title']}{fav_star}")
        print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

def view_detail():
    show_list()
    try:
        idx = int(input("\n번호 입력: ")) - 1
        if 0 <= idx < len(prompts):
            p = prompts[idx]
            print("\n" + "─" * 40)
            print(f"제목: {p['title']}")
            print(f"카테고리: {p['category']}")
            print(f"즐겨찾기: {'⭐' if p['favorite'] else 'X'}")
            print("─" * 40)
            print(f"내용:\n{p['content']}")
            print("─" * 40)
        else:
            print("❌ 존재하지 않는 번호입니다.")
    except ValueError:
        print("❌ 숫자만 입력 가능합니다.")

def toggle_favorite():
    show_list()
    try:
        idx = int(input("\n즐겨찾기 관리할 프롬프트 번호 입력: ")) - 1
        if 0 <= idx < len(prompts):
            prompts[idx]["favorite"] = not prompts[idx]["favorite"]
            status = "추가" if prompts[idx]["favorite"] else "해제"
            print(f"\n✅ '{prompts[idx]['title']}' 프롬프트를 즐겨찾기에 {status}했습니다!")
        else:
            print("❌ 존재하지 않는 번호입니다.")
    except ValueError:
        print("❌ 숫자만 입력 가능합니다.")

def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    favorites = [p for p in prompts if p["favorite"]]
    
    if not favorites:
        print("즐겨찾기된 프롬프트가 없습니다.")
    else:
        for i, p in enumerate(favorites, 1):
            print(f"{i}. [{p['category']}] {p['title']} ⭐")
        print(f"\n총 {len(favorites)}개의 즐겨찾기")

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            add_prompt()
        elif choice == '2':
            show_list()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            search_prompt()
        elif choice == '5':
            view_detail()
        elif choice == '6':
            toggle_favorite()
        elif choice == '7':
            show_favorites()
        elif choice == '0':
            print("👋 프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("❌ 잘못된 번호입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()