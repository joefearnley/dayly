import { FormMessage, Message } from "@/components/form-message";
import { SubmitButton } from "@/components/submit-button";
import { Input } from "@/components/ui/input";
import { TextArea } from "@/components/ui/text-area";
import { Label } from "@/components/ui/label";
import Link from "next/link";
import { createPost } from './actions';

export default async function CreatePost() {
  return (
    <form className="flex-1 flex flex-col min-w-64">
      <h1 className="text-2xl font-medium">Create Post</h1>
      <p className="text-sm text-foreground">
        Don't have an account?{" "}
        <Link className="text-foreground font-medium underline" href="/sign-up">
          Sign up
        </Link>
      </p>
      <div className="flex flex-col gap-2 [&>input]:mb-3 mt-8">
        <Label htmlFor="email">Title</Label>
        <Input name="title" placeholder="title" required />
        <div className="flex justify-between items-center">
          <Label htmlFor="password">Post</Label>
        </div>
        <TextArea name="body" placeholder="post body" required />
        <SubmitButton pendingText="Creating Post..." formAction={createPost}>
          Create Post
        </SubmitButton>
      </div>
    </form>
  );
}