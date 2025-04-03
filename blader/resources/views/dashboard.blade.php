<x-layouts.app :title="__('Dashboard')">
    <div class="flex w-full flex-1 flex-col gap-4 rounded-xl">
        <div class="my-4">
            <h1 class="my-2 text-3xl font-extrabold">Latest Entries</h1>
        </div>
    </div>

    <hr>

    <div>
        @if ($entries->isEmpty())
        <h3>No Entries Found</h3>
        <p><a href="{{ route('entries.create') }}">Create One</a></p>
        @else
            @foreach ($entries as $entry)
            <div class="mt-6">
                <p><a href="/entries/{{ $entry->slug }}" class="text-red-900 font-bold">{{ $entry->date_published  }}</a></p>
                <p>{{ $entry->body }}</p>
            </div>
            @endforeach
        @endif
    </div>
</x-layouts.app>
