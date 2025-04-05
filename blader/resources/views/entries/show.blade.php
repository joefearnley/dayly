<x-layouts.app :title="__('Dashboard')">
    <div class="flex h-full w-full flex-1 flex-col gap-4 rounded-xl">
        <div class="flex items-center justify-between">
            <h1 class="my-2 text-4xl font-extrabold">{{ $entry->date_published }}</h1>
        </div>

        <hr>

        <div class="flex flex-col items-center justify-center gap-4 p-6 md:p-10">
            <div class="flex w-full max-w-lg flex-col gap-2">
                {{ $entry->body }}
            </div>
        </div>
    </div>
</x-layouts.app>
