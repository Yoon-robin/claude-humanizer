import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { PostComposer } from "@/components/PostComposer";

describe("게시물 작성", () => {
  it("제목 없이 등록하면 안내 토스트를 띄운다", async () => {
    render(<PostComposer boardName="자유게시판" />);
    await userEvent.click(screen.getByText("등록"));
    expect(await screen.findByText("제목을 입력해 주세요.")).toBeInTheDocument();
  });

  it("등록에 성공하면 완료 토스트를 띄운다", async () => {
    render(<PostComposer boardName="자유게시판" />);
    await userEvent.type(screen.getByPlaceholderText("제목"), "첫 글");
    await userEvent.click(screen.getByText("등록"));
    expect(await screen.findByText("게시물이 성공적으로 등록되었습니다!")).toBeInTheDocument();
  });
});
