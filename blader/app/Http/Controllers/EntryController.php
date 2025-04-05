<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreEntryRequest;
use App\Http\Requests\UpdateEntryRequest;
use App\Models\Entry;
use Carbon\Carbon;

class EntryController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return view('entries.index', [
            'entries' => auth()->user()->entries()->latest()->paginate(10),
        ]);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return view('entries.create');
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreEntryRequest $request)
    {
        $data = $request->validated();
        $slug = Carbon::parse($data['date_published'])->format('Y-m-d') . '-' . uniqid();

        Entry::create([
            'body' => $data['body'],
            'date_published' => $data['date_published'],
            'user_id' => auth()->user()->id,
            'slug' => $slug,
        ]);

        return redirect()->route('entries.index')->with('success', 'Entry created successfully.');
    }

    /**
     * Display the specified resource.
     */
    public function show($slug)
    {
        $entry = Entry::where('slug', $slug)->firstOrFail();

        return view('entries.show', [
            'entry' => $entry,
        ]);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Entry $entry)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateEntryRequest $request, Entry $entry)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Entry $entry)
    {
        //
    }
}
