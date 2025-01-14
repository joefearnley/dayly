'use server'

import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'

import { createClient } from '@/utils/supabase/server'

export async function createPost(formData: FormData) {
  const supabase = await createClient()

  const data = {
    email: formData.get('title') as string,
    password: formData.get('body') as string,
  }

//   const { error } = await supabase.auth.signInWithPassword(data)

  if (error) {
    redirect('/error')
  }

  revalidatePath('/', 'layout')
  redirect('/')
}