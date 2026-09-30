"use client";
import { useState } from "react";
import { toast } from "@/lib/toast";
import { createPost, saveDraft } from "@/lib/posts";

const MAX_TITLE = 60;

export function PostComposer({ boardName }: { boardName: string }) {
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");

  async function onSaveDraft() {
    await saveDraft({ title, body });
    toast("임시 저장했어요.");
  }

  async function onSubmit() {
    if (!title.trim()) {
      toast("제목을 입력해 주세요.");
      return;
    }
    if (title.length > MAX_TITLE) {
      toast(`제목은 ${MAX_TITLE}자까지 쓸 수 있어요.`);
      return;
    }
    try {
      await createPost({ title, body });
      toast("게시물이 성공적으로 등록되었습니다!");
    } catch (err) {
      console.error("[PostComposer] 게시물 등록 실패", err);
      toast("글을 올리지 못했어요. 다시 시도해 주세요.");
    }
  }

  return (
    <form>
      <p>{boardName}에 글 쓰기</p>
      <input placeholder="제목" value={title} onChange={(e) => setTitle(e.target.value)} />
      <textarea
        placeholder="무슨 이야기를 나눠 볼까요?"
        value={body}
        onChange={(e) => setBody(e.target.value)}
      />
      <button type="button" onClick={onSaveDraft}>
        임시 저장
      </button>
      <button type="button" onClick={onSubmit}>
        등록
      </button>
    </form>
  );
}
