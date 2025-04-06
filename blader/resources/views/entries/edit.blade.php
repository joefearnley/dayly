<x-layouts.app :title="__('Dashboard')">
    <div class="flex h-full w-full flex-1 flex-col gap-4 rounded-xl">
        <div class="flex items-center justify-between">
            <h1 class="my-2 text-4xl font-extrabold">{{ __('Edit') }} - {{ $entry->date_published }}</h1>
        </div>

        <hr>

        <div class="flex flex-col items-center justify-center gap-4 p-6 md:p-10">
            <div class="flex w-full max-w-lg flex-col gap-2">
                <form action="{{ route('entries.update', $entry) }}" method="POST" class="flex flex-col gap-6">
                    @csrf
                    @method('patch')
                    <div class="relative">
                        <label
                            id="id_date_published"
                            for="date_published"
                            class="inline-flex items-center text-sm font-medium text-zinc-800 dark:text-white">
                            {{ __('Date') }}
                        </label>
                        <input
                            type="date"
                            required="required"
                            autofocus="autofocus"
                            placeholder="mm/dd/yyyy"
                            name="date_published"
                            id="date_published"
                            value="{{ $entry->datePublishedForForm() }}"
                            aria-required="true"
                            aria-labelledby="id_date_published"
                            class="w-full border rounded-lg block disabled:shadow-none dark:shadow-none appearance-none text-base sm:text-sm py-2 h-10 leading-[1.375rem] ps-3 pe-3 bg-white dark:bg-white/10 dark:disabled:bg-white/[7%] text-zinc-700 disabled:text-zinc-500 placeholder-zinc-400 disabled:placeholder-zinc-400/70 dark:text-zinc-300 dark:disabled:text-zinc-400 dark:placeholder-zinc-400 dark:disabled:placeholder-zinc-500 shadow-xs border-zinc-200 border-b-zinc-300/80 disabled:border-b-zinc-200 dark:border-white/10 dark:disabled:border-white/5"
                        />
                    </div>
                    <div class="relative">
                        <label
                            id="id_body"
                            for="body"
                            class="inline-flex items-center text-sm font-medium text-zinc-800 dark:text-white">
                            {{ __('Body') }}
                        </label>
                        <textarea
                            id="body"
                            name="body"
                            aria-required="true"
                            rows="20"
                            required="required"
                            placeholder="Write your entry here..."
                            aria-labelledby="id_body"
                            class="w-full border rounded-lg block disabled:shadow-none dark:shadow-none appearance-none text-base sm:text-sm py-2 h-100 leading-[1.375rem] ps-3 pe-3 bg-white dark:bg-white/10 dark:disabled:bg-white/[7%] text-zinc-700 disabled:text-zinc-500 placeholder-zinc-400 disabled:placeholder-zinc-400/70 dark:text-zinc-300 dark:disabled:text-zinc-400 dark:placeholder-zinc-400 dark:disabled:placeholder-zinc-500 shadow-xs border-zinc-200 border-b-zinc-300/80 disabled:border-b-zinc-200 dark:border-white/10 dark:disabled:border-white/5"
                        >
                        {{ $entry->body }}
                    </textarea>
                    </div>
                    <div class="flex items-center justify-end">
                        <flux:button variant="primary" type="submit" class="w-full">{{ __('Update Entry') }}</flux:button>

                        <flux:button variant="primary" type="submit" class="w-full">{{ __('Update Entry') }}</flux:button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</x-layouts.app>
