import Link from "next/link";
import { useTranslations } from "next-intl";
import { Bell, Menu, Search } from "lucide-react";

// 헤더는 모든 페이지 상단에 고정된다
export function Header({ unread }: { unread: number }) {
  const t = useTranslations("nav");
  return (
    <header>
      <button aria-label="메뉴 열기">
        <Menu />
      </button>
      <Link href="/">{t("home")}</Link>
      <button aria-label="검색">
        <Search />
      </button>
      <button aria-label="알림 목록을 열기 위한 버튼입니다">
        <Bell />
        {unread > 0 && <span aria-label={`읽지 않은 알림 ${unread}개`}>{unread}</span>}
      </button>
    </header>
  );
}
