<x-layouts.app :title="__('Dashboard')">
    <div class="flex h-full w-full flex-1 flex-col gap-4 rounded-xl">
        <div class="flex items-center justify-between">
            <h1 class="my-2 text-3xl font-extrabold">Entries</h1>
            <a href="{{ route('entries.create') }}" class="flex items-center justify-between gap-3 px-5 py-1.5 dark:text-[#EDEDEC] border-[#19140035] hover:border-[#1915014a] border text-[#1b1b18] dark:border-[#3E3E3A] dark:hover:border-[#62605b] rounded-sm text-sm leading-normal">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="inline-block size-4">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                </svg>
                <span>Add entry</span>
            </a>
        </div>

        <hr>

        @if (session()->has('message'))
        <div class="py-6 my-6">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <div class="rounded-lg bg-gray-700 px-6 py-5 text-base text-white flex justify-between" role="alert">
                    <div>Thios is the message</div>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 cursor-pointer">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </div>
            </div>
        </div>
        @endif

        <div>
        @if ($entries->isEmpty())
            <h3>No Entries Found</h3>
            <p class="mt-4"><a href="{{ route('entries.create') }}">Create One</a></p>
        @else
            @foreach ($entries as $entry)
            <div class="mt-6">
                <p><a href="{{ route('entries.show', $entry->slug) }}" class="text-red-900 font-bold">{{ $entry->date_published  }}</a></p>
                <p>{{ $entry->body }}</p>
            </div>
            @endforeach
        @endif
        </div>
    </div>
</x-layouts.app>
